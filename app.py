from flask import Flask, render_template, request, redirect, url_for
from devices import devices

app = Flask(__name__)

@app.route("/")
def dashboard():
    device_status = {name: dev.get_status() for name, dev in devices.items()}
    
    # Calculate total cost
    total_cost = sum(dev["cost"] for dev in device_status.values())
    
    return render_template("dashboard.html", devices=device_status, total_cost=total_cost)

@app.route("/toggle/<device_name>")
def toggle_device(device_name):
    device = devices.get(device_name)
    if device:
        if device.is_on:
            device.turn_off()
        else:
            device.turn_on()
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)
