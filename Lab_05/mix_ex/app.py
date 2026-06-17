from mix_portal.console_utf8 import configure_console_utf8
from mix_portal.server import create_app


configure_console_utf8()
app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
