from api.index import app

application = app
__all__ = [application]

if __name__ == "__main__":
    application.run()

