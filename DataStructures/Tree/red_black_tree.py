from DataStructures.Tree import rbt_node as rbt

def default_compare(key, element):
  node_key= element["key"]
  if key<node_key:
    return -1
  elif key>node_key:
    return 1
  else:
    return 0
  
def rotate_left(node_rbt):
  if node_rbt is None or node_rbt["right"] is None:
    return node_rbt
  
  new_root= node_rbt["right"]
  node_rbt["right"]= new_root["left"]
  new_root["left"]= node_rbt
  new_root["color"]= node_rbt["color"]
  node_rbt["color"]= "red"
  
  new_root["size"]= node_rbt["size"]
  size_left= size_tree(node_rbt["left"])
  size_right= size_tree(node_rbt["right"])
  node_rbt["size"]= 1 + size_left + size_right
  return new_root

def rotate_right(node_rbt):
  if node_rbt is None or node_rbt["left"] is None:
    return node_rbt
  new_root= node_rbt["left"]
  node_rbt["left"]= new_root["right"]
  new_root["right"]= node_rbt
  new_root["color"]= node_rbt["color"]
  node_rbt["color"]= "red"
  
  new_root["size"]= node_rbt["size"]
  size_left= size_tree(node_rbt["left"])
  size_right= size_tree(node_rbt["right"])
  node_rbt["size"]= 1 + size_left + size_right
  return new_root

def flip_node_color(node_rbt):
  if node_rbt["color"]=="red":
    node_rbt["color"]="black"
  else:
    node_rbt["color"]="red"
  return node_rbt

def flip_colors(node_rbt):
  node_rbt= flip_node_color(node_rbt)
  if node_rbt["left"] is not None:
    node_rbt["left"]= flip_node_color(node_rbt["left"])
  if node_rbt["right"] is not None:
    node_rbt["right"]= flip_node_color(node_rbt["right"])
  return node_rbt
  
def size_tree(node_rbt):
  if node_rbt is None:
    return 0
  else:
    return node_rbt["size"]
  
def insert_node(root, key, value):
  if root is None:
    return rbt.new_node(key, value)
  
  comp = default_compare(key, root)
  if comp<0:
    root["left"]= insert_node(root["left"], key, value)
  elif comp>0:
    root["right"]= insert_node(root["right"], key, value)
  else:
    root["value"]= value
  
  if rbt.is_red(root["right"]) and not rbt.is_red(root["left"]):
    root = rotate_left(root)
  if rbt.is_red(root["left"]) and rbt.is_red(root["left"]["left"]):
    root = rotate_right(root)
  if rbt.is_red(root["left"]) and rbt.is_red(root["right"]):
    root = flip_colors(root)
  
  root["size"]= 1 + size_tree(root["left"]) + size_tree(root["right"])
  return root

def put(my_rbt, key, value):
  my_rbt["root"]= insert_node(my_rbt["root"], key, value)
  if my_rbt["root"] is not None:
    my_rbt["root"]["color"]= "black"
  return my_rbt