from init import create_app

app = create_app('default')

if __name__ == '__main__':
    app.run('192.168.128.128')