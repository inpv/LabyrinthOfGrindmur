# LabyrinthOfGrindmur
<p>A turn-based roguelike maze runner against an AI-driven enemy.</p>
<p>Based on the classic roguelike <a href="http://rogueliketutorials.com/tutorials/tcod/v2/">tutorial</a> as well as the <a href="https://en.wikipedia.org/wiki/Labyrinth_(paper-and-pencil_game)">Labyrinth</a> pen-and-paper game and tailored for maze generation and AI maze solving.</p>

<p>The player has to solve the maze with limited visibility (Field of View) before the rival AI finds a way out of its own maze. However, the player is able to see the full enemy's map and thus may predict their moves.</p>
<p>The mazes are procedurally generated (by Recursive Backtracking algorithm) and have traps as well as buffs, which affect movement speed. Difficulty levels affect their chance of spawning.</p>
<p>The game itself is turn-based, like most classic roguelikes. Whoever starts traversing through the maze first is decided randomly.</p>
<p>The AI finds a solution for the maze using Recursive Backtracking algorithm and then starts moving through the map using the generated way. Any obstacles or buffs met are counted for the enemy as well.</p>
<img src="https://user-images.githubusercontent.com/68565248/141439637-abd4c415-540b-479e-bfce-bc90c4438c61.png" title="A screenshot from the game" alt="A screenshot from the game">
