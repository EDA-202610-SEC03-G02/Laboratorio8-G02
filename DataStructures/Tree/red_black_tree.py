def rotate_right(bst):
  root=bst["root"]
  izq= root["left"]
  if izq["color"]=="red" and izq["left"]["color"]=="red":
    if izq["right"] is not None: 
      temp= izq["right"]
      root["left"]=None
      izq["right"]=root
      root=izq
      root["right"]["left"]=temp #Primera version de rotate right