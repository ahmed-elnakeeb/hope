from simple_image_download import simple_image_download as simp 
response = simp.simple_image_download
response().download("one peice", 200, extensions={'.jpg', '.png', '.ico', '.gif', '.jpeg'})