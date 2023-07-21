const GRID_SIZE = 35; // Make the grid square, 35x35
const CLICK_PAUSE_DELAY = 100; // Delay in milliseconds to pause the game after a click
let grid = createGrid(GRID_SIZE);
let isPlaying = false;
let interval;
let lastClickTime = 0;
let manualPause = false; // Track if the game was manually paused by clicking the grid

function createGrid(size) {
  const grid = new Array(size);
  for (let i = 0; i < size; i++) {
    grid[i] = new Array(size).fill(false);
  }
  return grid;
}

function drawGrid() {
  const gridContainer = document.getElementById('grid');
  gridContainer.innerHTML = '';

  for (let i = 0; i < GRID_SIZE; i++) {
    for (let j = 0; j < GRID_SIZE; j++) {
      const cell = document.createElement('div');
      cell.classList.add('cell');
      cell.dataset.row = i;
      cell.dataset.col = j;
      cell.addEventListener('click', toggleCellState);
      if (grid[i][j]) {
        cell.classList.add('alive');
      }
      gridContainer.appendChild(cell);
    }
  }
}

function toggleCellState(event) {
  const currentTime = Date.now();
  if (currentTime - lastClickTime < CLICK_PAUSE_DELAY) {
    return;
  }
  lastClickTime = currentTime;

  const row = parseInt(event.target.dataset.row);
  const col = parseInt(event.target.dataset.col);

  if (isPlaying) {
    // If the game is playing and the grid is clicked, pause the game
    manualPause = true;
    pauseGame();
  } else {
    // If the game is not playing and the grid is clicked, toggle the cell state
    grid[row][col] = !grid[row][col];
    event.target.classList.toggle('alive');
  }
}

function updateGrid() {
  const newGrid = createGrid(GRID_SIZE);

  for (let i = 0; i < GRID_SIZE; i++) {
    for (let j = 0; j < GRID_SIZE; j++) {
      const neighbors = countAliveNeighbors(i, j);

      if (grid[i][j]) {
        // Any live cell with fewer than two live neighbors dies
        // Any live cell with two or three live neighbors lives on
        // Any live cell with more than three live neighbors dies
        newGrid[i][j] = neighbors === 2 || neighbors === 3;
      } else {
        // Any dead cell with exactly three live neighbors becomes alive
        newGrid[i][j] = neighbors === 3;
      }
    }
  }

  grid = newGrid;
  drawGrid();
}

function countAliveNeighbors(row, col) {
  let count = 0;

  for (let i = -1; i <= 1; i++) {
    for (let j = -1; j <= 1; j++) {
      if (i === 0 && j === 0) continue;

      const newRow = row + i;
      const newCol = col + j;

      if (newRow >= 0 && newRow < GRID_SIZE && newCol >= 0 && newCol < GRID_SIZE) {
        count += grid[newRow][newCol] ? 1 : 0;
      }
    }
  }

  return count;
}

function startGame() {
  if (!isPlaying) {
    isPlaying = true;
    manualPause = false;
    delayedUpdate(); // Use delayedUpdate() to update the grid with a delay
    updateIndicator();
  }
}

function pauseGame() {
  if (isPlaying) {
    isPlaying = false;
    updateIndicator();
  }
}

function clearGrid() {
  for (let i = 0; i < GRID_SIZE; i++) {
    for (let j = 0; j < GRID_SIZE; j++) {
      grid[i][j] = false;
    }
  }
  drawGrid(); // Redraw the grid to remove the "alive" class from all cells
}

function updateIndicator() {
  const indicator = document.getElementById('indicator');
  indicator.textContent = isPlaying ? 'Playing' : 'Paused';
}

function delayedUpdate() {
  if (!isPlaying) return;

  if (manualPause) {
    manualPause = false;
    return;
  }

  updateGrid();
  updateIndicator();
  setTimeout(delayedUpdate, 200);
}

document.body.addEventListener('click', function (event) {
  const gridContainer = document.getElementById('grid');
  const clickedElement = event.target;
  if (!gridContainer.contains(clickedElement)) {
    // If the click occurs outside the grid, start the game
    startGame();
  }
});

// Initialize the grid
drawGrid();
