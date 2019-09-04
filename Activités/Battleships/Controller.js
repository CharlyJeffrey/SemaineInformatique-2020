/*
    Game Controller
*/

var gameController = (function() {
    // Cell object
    var Cell = function(posX, posY) {
        // Position in the grid
        this.x = posX;
        this.y = posY;
        // Has a ship
        this.has_ship = false;
        // Has been hit yet
        this.has_been_hit = false;
        // ID
        this.id = String(posX) +""+ String(posY);
    };

    // Getter functions
    Cell.prototype.getId = function() {return this.id;};
    Cell.prototype.HasBeenHit = function() {return this.has_been_hit;};
    Cell.prototype.HasShip = function() {return this.has_ship;};

    // Setter functions
    Cell.prototype.SetShip = function(value) {this.has_ship = value;};

    // Function when the case has been hit
    Cell.prototype.Hit = function() {
        if (!this.has_been_hit) {
            this.has_been_hit = true;
            return this.has_ship;
        } else {
            console.log("Case has already been hit.");
            return false;
        }
    };

    // Grid object
    var Grid = function(ships_position) {
        // Dimension of the grid
        this.rows = config.shape[0];
        this.cols = config.shape[1];

        // Initialize the score
        this.score = 0;
        
        // Initialise the grid
        this.grid = new Array(this.rows);
        for (var i = 0; i < this.rows; i++) this.grid[i] = new Array(this.cols);

        for (var i = 0; i < this.rows; i++) {
            for (var j = 0; j < this.cols; j++) {
                this.grid[i][j] = new Cell(i, j);
            }
        }

        // Place the boat
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
    Grid.prototype.getCase = function(i, j) {return this.grid[i][j];}
    Grid.prototype.getShape = function() {return config.shape;}
    Grid.prototype.getRow = function(i) {return this.grid[i];}
    Grid.prototype.getCol = function(j) {
        var col = new Array(this.rows);
        for (var i = 0; i < this.rows; i++) col[i] = this.grid[i][j];
        return col;
    }

    // Function to hit a case and update score
    Grid.prototype.hitCell = function(i, j) { if (this.grid[i][j].Hit()) this.score++; }

    // Function to get the case's state
    Grid.prototype.GetCaseState = function(i, j) {
        if (!this.grid[i][j].HasBeenHit()) {
            return "default";
        } else if (this.grid[i][j].HasShip()) {
            return "hit";
        } else {
            return "miss";
        }
    }


    return {
        // Initialize a new grid
        newGrid : function(ships) {
            return new Grid(ships);
        },
    };
})();

var UIController = (function() {
    var DOMstrings = {
        // Grid container
        gridContainer: ".grid-container",
        shipContainer: ".ship-container",
        // Score
        scoreValue: ".score-value",
        // Refresh button
        refreshBtn: ".refresh-btn",
        // Show solution button
        solutionBtn: ".solution-btn",
        // Team selection
        selectTeam: "my-select",
        // State
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
        toggleCase: function(cellID, state_prev, state_post) {
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


var mainController = (function(gameCtrl, UICtrl) {
    var grid, grid_active, boat_down;

    var DOM = UICtrl.getDOMstrings();

    // Setup all of the event listener
    var setupEventListener = function() {
        // Grid interaction
        document.querySelector(DOM.gridContainer).addEventListener("click", interaction);
        // Button interaction
        document.querySelector(DOM.solutionBtn).addEventListener("click", showSolution);
        document.querySelector(DOM.refreshBtn).addEventListener("click", refresh);
    };

    // Setup all the interactions with the player
    var interaction = function(event) {
        var itemID, posX, posY, state_one, state_two;

        if (!grid_active) return;

        // Get the ID of the corresponding item
        itemID = event.target.id;

        if (itemID) {
            // Get relative position
            posX = parseInt(itemID[0]);
            posY = parseInt(itemID[1]);

            // Get the state
            state_one = grid.GetCaseState(posX, posY);

            // Hit the case
            grid.hitCell(posX, posY);
            // Get the state
            state_two = grid.GetCaseState(posX, posY);

            // Toggle between the states
            UICtrl.toggleCase(itemID, state_one, state_two)

            // Remove ship
            if (grid.getCase(posX, posY).HasShip()) {
                UICtrl.shipDown(boat_down++);
            }
        }
        return;
    };

    // Show the solution of the current team number
    var showSolution = function(event) {
        let c, state, id;
        // Shape of the grid
        var shape = grid.getShape();
        // Loop over all the cases
        for (let i = 0; i < shape[0]; i++) {
            for (let j = 0; j < shape[1]; j++) {
                // Obtain the case
                c = grid.getCase(i, j);
                // Obtain the state
                state = grid.GetCaseState(i, j);
                // Case ID
                id = i + "" + j;
                
                switch (state) {
                    case "miss":
                        UICtrl.toggleCase(id, state, "default");
                        break;
                    
                    case "default":
                        if (c.HasShip()) UICtrl.toggleCase(id, state, "hit");
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