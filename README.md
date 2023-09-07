# fire_detection_YOLOv8

Code for learning fire detection using Yolov8.

To actually implement it, we used the flask library to build a local service on server.py .


## Configuring Code Execution Environment

You must perform the following steps to execute the code:

Install the required libraries (ultralytics, torch, PIL, flask, waitress).
Copy the code and save it as a Python script file.
A separate index.html file is required, so create that file as well.
Launch Web Server:

Open the terminal and navigate to the directory where the script files are located.

Run the web server using the following command:

python server.py

## Accessing Web Pages

If the web server is running, go to the following address from your browser: http://localhost:12321

## Using Web Pages

When you access the web page, you will see a simple screen where you can upload an image.
Click the "Choose File" button to select an image file on your computer.
Select the image and click the "Predict" button.
The server processes the image and visualizes the original image and object detection results together.

example
![example](https://github.com/Mutoy-choi/fire_detection_YOLOv8/assets/87027571/e82135d7-314b-4750-84d3-16b0e1f628ae)


## Shutting down the website

After checking the web page, you can exit the web server by pressing Ctrl+C at the terminal if you want.

https://drive.google.com/file/d/1Q9E67OtuaZIKlYsaG2VZb2cNES-73O1O/view?usp=drive_link
Link to best.pt .
