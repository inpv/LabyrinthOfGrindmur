# LabyrinthOfGrindmur
<p>A turn-based roguelike maze runner against an AI-driven enemy.</p>
<p>Based on the classic roguelike <a href="http://rogueliketutorials.com/tutorials/tcod/v2/">tutorial</a> as well as the <a href="https://en.wikipedia.org/wiki/Labyrinth_(paper-and-pencil_game)">Labyrinth</a> pen-and-paper game and tailored for maze generation and AI maze solving.</p>

<p>The player has to solve the maze with limited visibility (Field of View) before the rival AI finds a way out of its own maze. However, the player is able to see the full enemy's map and thus may predict their moves.</p>
<p>The mazes are procedurally generated (by Recursive Backtracking algorithm) and have traps as well as buffs, which affect movement speed. Difficulty levels affect their chance of spawning.</p>
<p>The game itself is turn-based, like most classic roguelikes. Whoever starts traversing through the maze first is decided randomly.</p>
<p>The AI finds a solution for the maze using Recursive Backtracking algorithm and then starts moving through the map using the generated way. Any obstacles or buffs met are counted for the enemy as well.</p>
<img src="https://user-images.githubusercontent.com/68565248/141439637-abd4c415-540b-479e-bfce-bc90c4438c61.png" title="A screenshot from the game" alt="A screenshot from the game">

<p><b>The story</b></p>
<p><i>(based on <a href="https://keygard.bandcamp.com/">Keygard</a> fantasy story series)</i></p>

<p>Unexpectedly, the forest citadel of the Murk Elves has been besieged by the powers of darkness led by Larutiore, a crafty undead thief looking to summon the ancient evil spirits of his mentor, the Great Serpent Grindmur.</p>
<p>The latter, fortunately, has been sleeping in the soil for ages and built a series of mazes to deceive possible trespassers. With Larutiore and his minions on the march, the city was quickly destroyed and the elves gone into hiding underground, in the vast grottos beneath their city.</p>
<p>Little they know, that in the very same grottos exists an entrance to the final maze, leading to the room where Grindmur himself sleeps, and Larutiore has already entered that maze..</p>
<p>Thus, time is running out quickly for the Elven King leading whatever is left of the squad to find reinforcements. If he succeeds before Larutiore finds Grindmur, the elves have a chance, otherwise their world is completely and utterly doomed.</p>
