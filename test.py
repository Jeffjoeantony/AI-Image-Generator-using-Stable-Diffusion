from PIL import Image, ImageDraw

# Step 1: Open and resize the image
img = Image.open("D:/AJCE/1692089610777 (1).jpg").resize((200, 200)).convert("RGBA")

# Step 2: Create a circular mask
mask = Image.new("L", (200, 200), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 200, 200), fill=255)

# Step 3: Apply the circular mask
circular_img = Image.new("RGBA", (200, 200))
circular_img.paste(img, (0, 0), mask=mask)

# Step 4: Save and show the result
circular_img.save("circular_photo.png")
circular_img.show()
