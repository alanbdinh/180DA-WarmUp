import cv2
import numpy as np

# code adapted from example in https://docs.opencv.org/4.5.3/da/d97/tutorial_threshold_inRange.html
# boundingRect portion adapted from https://code.adonline.id.au/bounding-rectangles-in-python-opencv/

# operating constants
max_value = 255
low_B = 0; low_G = 0; low_R = 0;
high_B = max_value; high_G = max_value; high_R = max_value;
window_detection_name = 'Object Detection'
low_B_name = 'Low B'; low_G_name = 'Low G'; low_R_name = 'Low R';
high_B_name = 'High B'; high_G_name = 'High G'; high_R_name = 'High R';

# trackbar functions
def on_low_B_thresh_trackbar(val):
    global low_B
    global high_B
    low_B = val
    low_B = min(high_B-1, low_B)
    cv2.setTrackbarPos(low_B_name, window_detection_name, low_B)
def on_high_B_thresh_trackbar(val):
    global low_B
    global high_B
    high_B = val
    high_B = max(high_B, low_B+1)
    cv2.setTrackbarPos(high_B_name, window_detection_name, high_B)
def on_low_G_thresh_trackbar(val):
    global low_G
    global high_G
    low_G = val
    low_G = min(high_G-1, low_G)
    cv2.setTrackbarPos(low_G_name, window_detection_name, low_G)
def on_high_G_thresh_trackbar(val):
    global low_G
    global high_G
    high_G = val
    high_G = max(high_G, low_G+1)
    cv2.setTrackbarPos(high_G_name, window_detection_name, high_G)
def on_low_R_thresh_trackbar(val):
    global low_R
    global high_R
    low_R = val
    low_R = min(high_R-1, low_R)
    cv2.setTrackbarPos(low_R_name, window_detection_name, low_R)
def on_high_R_thresh_trackbar(val):
    global low_R
    global high_R
    high_R = val
    high_R = max(high_R, low_R+1)
    cv2.setTrackbarPos(high_R_name, window_detection_name, high_R)
	
# set up windows and trackbars
cv2.namedWindow(window_detection_name)
cv2.createTrackbar(low_B_name, window_detection_name , low_B, max_value, on_low_B_thresh_trackbar)
cv2.createTrackbar(high_B_name, window_detection_name , high_B, max_value, on_high_B_thresh_trackbar)
cv2.createTrackbar(low_G_name, window_detection_name , low_G, max_value, on_low_G_thresh_trackbar)
cv2.createTrackbar(high_G_name, window_detection_name , high_G, max_value, on_high_G_thresh_trackbar)
cv2.createTrackbar(low_R_name, window_detection_name , low_R, max_value, on_low_R_thresh_trackbar)
cv2.createTrackbar(high_R_name, window_detection_name , high_R, max_value, on_high_R_thresh_trackbar)

# leveling using inrange to check Red level in RGB.
cap = cv2.VideoCapture(0)
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read() # frame should already be in BGR right?
	filtered = cv2.inRange(frame, (low_B, low_G, low_R), (high_B, high_G, high_R))
	x1,y1,w,h = cv2.boundingRect(filtered)
	x2 = x1+w
	y2 = y1+h
	cv2.rectangle(frame, (x1, y1), (x2, y2), [255, 0, 0]) # draw blue rect
	# Display the resulting frame
	cv2.imshow('result frame', frame)
	# Display video stream with threshold applied
	cv2.imshow('after filter', filtered)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()