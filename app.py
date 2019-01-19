from flask import Flask, render_template, request

@app.route("/")
def index():
    return "Running"
