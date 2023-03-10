import cv2

image = cv2.imread("solar-system.jpg")

cv2.putText(
    image,
    "Sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    image,
    "Mercury",
    (120,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    image,
    "Venus",
    (150,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    image,
    "Earth",
    (175,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    image,
    "Mars",
    (300,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    image,
    "Jupiter",
    (350,250),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    image,
    "Saturn",
    (450,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    image,
    "Uranus",
    (550,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)
cv2.putText(
    image,
    "Neptune",
    (650,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,225)
)

cv2.imshow("Solar_System",image)

cv2.waitKey(0)