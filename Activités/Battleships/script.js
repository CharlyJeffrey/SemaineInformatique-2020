// VARIABLES-CONSTANTES GLOBALES

/* config.json */
const NBR_TEAM = config.nteam;
const NBR_SHIPS = config.nships;
const CHAR = config.char;
const GRID_CHAR = config.grid;
const GRID_SHAPE = config.shape;
const SOLUTIONS = config.coords

/* interface */
var DISPLAYED_TEAM = 0;     // Par défaut
var SCORE = 0;              // Par défaut
var SHIPS_LEFT = NBR_SHIPS; // Par défaut

console.log(config);

mainController.init(SOLUTIONS[0], NBR_SHIPS);


