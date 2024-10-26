# styleconvertor
.csv to .json /.json to .csv: Converts Forge/A1111 styles for ComfyUI styler nodes, and vice-versa

# What It Does
Converts formatting of the styles for direct use in Forge or ComfyUi stylers (Mile high Styler)
# How to Use
1. download the styleconvertor.py file to a folder with your styles.csv or .json files
2. backup the original style files (just for a good feeling)
3. run terminal from the folder, in Windows with ```cmd``` command
4. In terminal, write command  ```python styleconvertor.py```
5. Follow the instructions.

# How to Load Your Styles 
A. Forge (.csv): Copy styles.csv into the main folder (file must be named styles.csv)

B. ComfyUI (.json):
1. Install ComfyUI_MileHighStyler via Manager
2. Go to \ComfyUI\custom_nodes\ComfyUI_MileHighStyler\data and create a folder Your_stylename
3. Copy Your_stylename.json into Your_stylename folder
4. Update and restart ComfyUI
5. Double-click the workspace and **Search Nodes** for Your_stylename node, which is now ready to use (also the Advanced version)  

