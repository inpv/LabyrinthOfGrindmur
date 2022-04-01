# LabyrinthOfGrindmur
<p>A WIP turn-based roguelike maze runner against an AI-driven enemy.</p>
<p>Based on the classic roguelike <a href="http://rogueliketutorials.com/tutorials/tcod/v2/">tutorial</a> as well as the <a href="https://en.wikipedia.org/wiki/Labyrinth_(paper-and-pencil_game)">Labyrinth</a> pen-and-paper game and tailored for maze generation and AI maze solving.</p>

<p>The player has to solve the maze with limited visibility (Field of View = 1 cell ahead) before the rival AI reaches the end of its own maze. However, the player is able to see the full enemy's map and thus may predict their moves.</p>
<p>The mazes are procedurally generated (originally by Recursive Backtracking, but one can use any maze generation algorithm that yields a 2d array of wall/maze to be converted later into tiles) and have traps as well as buffs, which affect movement speed. Difficulty levels affect their chance of spawning.</p>
<p>The game itself is turn-based, like most classic roguelikes. Whoever starts traversing through the maze first is decided randomly.</p>
<p>The AI finds a solution for the maze using Recursive Backtracking algorithm (again, any can be used as long as it can find a way in a perfect maze) and then starts moving through the map using the generated way. Any obstacles or buffs met are counted for the enemy as they traverse the maze as well.</p>
<img src="https://user-images.githubusercontent.com/68565248/161261114-6cd8d80d-7201-40a4-b833-f0598eba21a0.png" title="A screenshot from the game" alt="A screenshot from the game">


<p><b>The story</b></p>
<p><i>(based on <a href="https://keygard.bandcamp.com/">Keygard</a> fantasy story series)</i></p>

<p>Unexpectedly, the forest citadel of the Murk Elves has been besieged by the powers of darkness led by Larutiore, a crafty undead thief looking to summon the ancient evil spirits of his mentor, the Great Serpent Grindmur.</p>
<p>The latter, fortunately, has been sleeping in the soil for ages and built a series of mazes to deceive possible trespassers. With Larutiore and his minions on the march, the city was quickly destroyed and the elves gone into hiding underground, in the vast grottos beneath their city.</p>
<p>Little they know, that in the very same grottos exists an entrance to the final maze, leading to the room where Grindmur himself sleeps, and Larutiore has already entered that maze..</p>
<p>Thus, time is running out quickly for the Elven King leading whatever is left of his squad to find reinforcements. If he succeeds before Larutiore finds Grindmur, the elves have a chance, otherwise their world is completely and utterly doomed.</p>

<p><b>Status on 09.01.22</b></p>
<p>The game itself is playable in PyCharm but the enemy doesn't move yet.</p>

<p><b>Status on 31.03.22</b></p>
<p>The alpha is fully playable, both in PyCharm and in the build.</p>
