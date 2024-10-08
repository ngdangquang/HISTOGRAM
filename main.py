import cv2
from matplotlib import pyplot as plt

img = cv2.imread('fish.jpg', 1)
channels = cv2.split(img)
colors = ('b', 'g', 'r')
channel_names = ('Blue', 'Green', 'Red')

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Image')
plt.axis('off')

plt.subplot(1, 2, 2)
for (channel, color, name) in zip(channels, colors, channel_names):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color=color, label=name)

plt.title('Histogram for color image')
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
