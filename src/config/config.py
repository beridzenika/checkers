screen_size = 640
piece_size = 64
board_size = 8
rows = 3
piece_fix = 4
border = 20
pos_fix = (screen_size-piece_size * board_size)/2
margin = pos_fix - border

checker_size = piece_size-2*piece_fix

white_color = "#ff9f50"
black_color = "#212121"
border_color = "#ce6030"
select_color = "#1E365A"
wood_color = "#e27f3d"
back_color = "#496648"

turn = 0
player = "red"
players = ["red", "black"]

icon = "king-red"

directions = [(1,1),(-1,1),(-1,-1),(1,-1)]