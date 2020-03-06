// Game Controller
var gameController = (function() {
    // Cell object
    var Cell = function(posX, posY) {
        // Position dans la grille
        this.x = posX;
        this.y = posY;
        this.has_ship = false;
        this.has_been_hit = false;
        this.id = String(posX) +""+ String(posY);
    };

    // Getter functions
    Cell.prototype.getId = function() {return this.id;};
    Cell.prototype.getState = function() {
        if (!this.has_been_hit) {
            return "default";
        } else if (this.has_ship) {
            return "hit";
        } else {
            return "miss";
        }
    }
    Cell.prototype.HasBeenHit = function() {return this.has_been_hit;};
    Cell.prototype.HasShip = function() {return this.has_ship;};

    // Setter functions
    Cell.prototype.SetShip = function(value) {this.has_ship = value;};

    // Fonction lorsqu'une case se fait touchée
    Cell.prototype.Hit = function() {
        if (!this.has_been_hit) {
            this.has_been_hit = true;
            return this.has_ship;
        } else {
            console.log("Cell has already been hit.");
            return false;
        }
    };

    // Grid object
    var Grid = function(ships_position) {
        // Dimension de la grille
        this.rows = config.shape[0];
        this.cols = config.shape[1];
        
        // Initialise la grille
        this.grid = new Array(this.rows);
        for (var i = 0; i < this.rows; i++) {
            this.grid[i] = new Array(this.cols);
            for (var j = 0; j < this.cols; j++) {
                this.grid[i][j] = new Cell(i, j);
            }
        }

        // Place les bateaux
        var index, row, col;
        ships_position.forEach(ship => {
            index = 1 * ship;
            row = 0;
            col = 0;
            
            while (index > this.cols - 1) {
                index = index - this.cols;
                row++;
            }
            col = index;
            this.grid[row][col].SetShip(true);
        });
    };

    // Getter functions
    Grid.prototype.getScore = function() {return this.score;}
    Grid.prototype.getCell = function(i, j) {return this.grid[i][j];}
    Grid.prototype.getShape = function() {return config.shape;}
    Grid.prototype.getRow = function(i) {return this.grid[i];}
    Grid.prototype.getCol = function(j) {
        var col = new Array(this.rows);
        for (var i = 0; i < this.rows; i++) col[i] = this.grid[i][j];
        return col;
    }

    // Function to hit a cell and update score
    Grid.prototype.hitCell = function(i, j) { if (this.grid[i][j].Hit()) this.score++;}

    // Function to get the cell's state
    Grid.prototype.GetCellState = function(i, j) { return this.grid[i][j].getState(); }


    return {
        // Initialize a new grid
        newGrid : function(ships) {
            return new Grid(ships);
        },
    };
})();

// UI Controller
var UIController = (function() {
    var DOMstrings = {
        // Grid container
        gridContainer: ".grid-container",
        shipContainer: ".ship-container",
        // Score
        scoreValue: ".score-value",
        // Refresh button
        refreshBtn: ".refresh-btn",
        // Vefify solution button
        checkBtn: ".check-btn",
        // Show solution button
        solutionBtn: ".solution-btn",
        // Team selection
        selectTeam: "my-select",
        // State
        shotImage: "shot",
        hitImage: "hit",
        missImage: "miss",
        defaultImage: "default",
    };

    return {
        // Access to the DOM
        getDOMstrings: function() {return DOMstrings;},

        // Setup the gridhit
        setupGrid: function(grid, nships) {
            var shape, itemHTML, gridDOM, shipDOM, cellNode;

            // Obtain the shape
            shape = grid.getShape();

            // Get the DOMs
            gridDOM = document.querySelector(DOMstrings.gridContainer);
            shipDOM = document.querySelector(DOMstrings.shipContainer);

            // Clear the grids
            while (gridDOM.firstChild) gridDOM.removeChild(gridDOM.firstChild);
            while (shipDOM.firstChild) shipDOM.removeChild(shipDOM.firstChild);


            // Setup the grid cells
            for (var i = 0; i < shape[0]; i++) {
                for (var j = 0; j < shape[1]; j++) {
                    itemHTML = '<div class="grid-item default" id='+i+j+'></div>';
                    gridDOM.insertAdjacentHTML("beforeend", itemHTML)
                }
            }

            for (var i = 0; i < nships; i++) {
                itemHTML = '<div class="ship-item boat" id="boat-'+i+'"></div>';
                shipDOM.insertAdjacentHTML("beforeend", itemHTML);
            }
        },

        // Toggle the between 'hit' or 'miss'
        toggleCell: function(cellID, state_prev, state_post) {
            if (state_prev == state_post) return;
            // Get the element
            cell = document.getElementById(cellID);
            // Change the state
            cell.classList.remove(state_prev);
            cell.classList.add(state_post);
        },

        toggleState: function(cellID, state) {
            // Get the element
            cell = document.getElementById(cellID);
            // Change cell state
            cell.classList.add(state);
        },

        shipDown: function(shipID) {
            // Get the boat id
            let ID = "boat-"+shipID;
            // Get element
            let shipDOM = document.getElementById(ID);
            // Switch image
            shipDOM.classList.remove("boat");
            shipDOM.classList.add("boat-down");
        },

        // Remove a ship
        removeShip: function() {
            var shipDOM;
            shipDOM = document.querySelector(DOMstrings.shipContainer);
            shipDOM.removeChild(shipDOM.lastChild);
            shipDOM.app
        },

        setupGame: function(grid, nships) {
            this.setupGrid(grid, nships);
        }
    }
})();

// App Controller
var mainController = (function(gameCtrl, UICtrl) {
    var grid, grid_active, cells_shot, boat_down;

    var DOM = UICtrl.getDOMstrings();

    // Setup all of the event listener
    var setupEventListener = function() {
        // Grid interaction
        document.querySelector(DOM.gridContainer).addEventListener("click", interaction);
        // Button interaction
        document.querySelector(DOM.checkBtn).addEventListener("click", checkShots);
        document.querySelector(DOM.solutionBtn).addEventListener("click", showSolution);
        document.querySelector(DOM.refreshBtn).addEventListener("click", refresh);
    };

    // Setup all the interactions with the player
    var interaction = function(event) {
        var itemID, posX, posY, state_one;

        if (!grid_active) return;

        // Get the ID of the corresponding item
        itemID = event.target.id;

        if (itemID) {
            // Get relative position
            posX = parseInt(itemID[0]);
            posY = parseInt(itemID[1]);

            // Gete the cell
            let cell = grid.getCell(posX, posY);

            if (!cell.HasBeenHit()) {
                // Add cell to list
                cells_shot.push(cell);
                // Get the state
                state_one = cell.getState();
                // Hit the cell
                grid.hitCell(posX, posY)
                // Toggle between the states
                UICtrl.toggleCell(itemID, state_one, "shot")
            }
        }
        return;
    };

    // Compare the answers and the solution
    var checkShots = function(event) {
        if (!grid_active) return;
        let state;
        // Loop over the cells who has been shot at
        cells_shot.forEach(cell => {
            state = cell.getState();

            if (state == "hit") {
                UICtrl.toggleCell(cell.getId(), "shot", "hit");
            } else {
                UICtrl.toggleCell(cell.getId(), "shot", "miss");
            }
        });
        // Desactivate the grid
        grid_active = false;

    };

    // Show the solution of the current team number
    var showSolution = function(event) {
        let cell;
        // Loop over all the cells of the grid
        for (let i = 0; i < grid.rows; i++) {
            for (let j = 0; j < grid.cols; j++) {
                // Obtain the cell
                cell = grid.getCell(i, j);
                // Verify if the cell has a boat
                if (cell.HasShip()) {
                    // Toggle cell image to a checkmark
                    UICtrl.toggleCell(cell.getId(), cell.getState(), "hit");
                } else {
                    // Hide the cell
                    UICtrl.toggleCell(cell.getId(), cell.getState(), "default");
                }
            }
        }
        // Desactivate the grid
        grid_active = false;
    }

    // Refresh button interaction
    var refresh = function(event) {
        // Get the select environnement
        var sel = document.getElementById(DOM.selectTeam);
        // Obtain the team number
        var team = parseInt(sel.value);
        if (team != 0) {
            // Get the team solution
            var sol = config.coords[team];
            // Initialize a new instance with the selected team
            setup(sol, sol.length);
        }
    }

    // Initialize a new grid
    var setup = function(ships_pos, nships) {
        grid = gameCtrl.newGrid(ships_pos);
        grid_active = true;
        cells_shot = [];
        boat_down = 0;

        UICtrl.setupGame(grid, nships);
    };

    return {
        init: function(ships, nships) {
            setup(ships, nships);
            setupEventListener();
        }
    };

})(gameController, UIController);