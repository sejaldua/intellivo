from intellivo_package import app, socketio
import os

# run the app 
if __name__ == '__main__':
    # init_db()
    # Change the debug to False when deploying to production
    socketio.run(app, debug=False)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port = port)
