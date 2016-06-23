# nbmg
NodeBasedRPGMapGenerator

# About

This project is a collection of Python functions that can be used to generate graph- (or node-) based maps of dungeons or adventure locations for tabletop fantasy roleplaying games. In contrast to classical dungeon generators this app does not create square-based maps or combinations of geomorphs, but instead randomly selects room descriptions and combines them with passage descriptors. The resulting graph is enriched with circular connections to make the dungeon more complex, and to provide shortcuts or alternative routes.

The inspiration for this app can be found in the following blog posts:

http://hillcantons.blogspot.de/2014/11/pointcrawl-series-index.html
http://thealexandrian.net/wordpress/13085/roleplaying-games/jaquaying-the-dungeon

A very similar app that already works in the browser can be found here:

http://meta-studios.com/dg/dungen.html

# How to use

1. Run the script in a Python environment. You can either use any free distribution or even use an Online App like https://trinket.io/.
2. Copy the resulting graph output to a visualizer that understand the Dot language like graphviz. You can also use the Online-App http://www.webgraphviz.com/ to quickly visualize the map.
3. Use the map to spark your imagination for story-based dungeon delving.
