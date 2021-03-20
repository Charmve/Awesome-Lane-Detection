# import cv2 as cv
# import numpy as np
# # import matplotlib.pyplot as plt

# def do_canny(frame):
#     gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
#     blur = cv.GaussianBlur(gray, (5, 5), 0)
#     canny = cv.Canny(blur, 50, 150)
#     return canny

# def do_segment(frame):
#     height = frame.shape[0]
#     polygons = np.array([
#                             [(0, height), (800, height), (380, 290)]
#                         ])
#     mask = np.zeros_like(frame)
#     cv.fillPoly(mask, polygons, 255)
#     segment = cv.bitwise_and(frame, mask)
#     return segment

# cap = cv.VideoCapture("input.mp4")
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     canny = do_canny(frame)
#     # plt.imshow(frame)
#     # plt.show()
#     segment = do_segment(canny)

    # cv.HoughLinesP(frame, distance resolution of accumulator in pixels (larger = less precision), angle resolution of accumulator in radians (larger = less precision), threshold of minimum number of intersections, empty placeholder array, minimum length of line in pixels, maximum distance in pixels between disconnected lines)
    hough = cv.HoughLinesP(segment, 2, np.pi / 180, 100, np.array([]), minLineLength = 100, maxLineGap = 50)

#     if cv.waitKey(10) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()
