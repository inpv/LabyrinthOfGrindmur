# LabyrinthOfGrindmur
<p>A turn-based roguelike maze runner against an AI-driven enemy.</p>
<p>Based on the classic roguelike <a href="http://rogueliketutorials.com/tutorials/tcod/v2/">tutorial</a> and tailored for maze generation and AI maze solving.</p>

<p>The player has to solve the maze with limited visibility (Field of View) before the rival AI finds a way out of the same maze. However, the player is able to see the full enemy's map.</p>
<p>The mazes are identical and have traps as well as buffs, which affect movement speed. Difficulty levels affect the chance of their spawning.</p>
<p>The game itself is turn-based, like most classic roguelikes. Whoever starts first is decided randomly.</p>
<p>The AI finds a solution for the maze using the Recursive Backtracking algorithm and then starts moving through the map using the way. Any obstacles or buffs met are counted for the enemy as well.</p>
<img src="https://user-images.githubusercontent.com/68565248/141386974-578efaaa-87a4-4288-befd-28f12f1c0382.png" title="A screenshot from the game" alt="A screenshot from the game">
