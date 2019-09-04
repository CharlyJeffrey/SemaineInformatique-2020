class Battleship {

    constructor(row_char, col_char, nships) {
        // Attributs de base
        this.row = new Array(row_char.length * (row_char.length - 1));
        this.col = new Array(col_char.length);
        this.nships = nships;
        this.char = col_char.concat(row_char);

        // Obtient les caractères possibles pour les rangées
        let index = 0;
        for (let i = 0; i < row_char.length; i++) {
            for (let j = 0; j < row_char.length; j++) {
                if (row_char[i] != row_char[j]) {
                    this.row[index++] = row_char[i].concat(row_char[j]);
                }  
            }        
        }
        
        for (let i = 0; i < col_char.length; i++) this.col[i] = col_char[i];

        // Grille de jeu
        this.grid = new Array(this.row.length * this.col.length);
        for (let i = 0; i < this.row.length; i++) {
            for (let j = 0; j < this.col.length; j++) {
                this.grid[i*this.col.length + j] = this.row[i].concat(this.col[j]);
            }
        }

        // Mapping char -> binaire
        this.map = new Map();
        const size = Math.floor(Math.log2(this.char.length));

        let p, n, tmp;
        for (let i = 0; i < this.char.length; i++) {
            p = size;
            n = i;
            tmp = "";

            while (p >= 0) {
                if (n - Math.pow(2, p) >= 0) {
                    tmp = tmp.concat('1');
                    n = n - Math.pow(2, p);
                } else {
                    tmp = tmp.concat('0');
                }
                p--;
            }
            while (tmp.length < size) {
                tmp = '0'.concat(tmp);
            }
            this.map.set(this.char[i], tmp);
        }

        console.log(this.map);
    }

    printGrid() {
        let _;
        for (let i = 0; i < this.row.length; i++) {
            _ = "";
            for (let j = 0; j < this.col.length; j++) {
                _ = _.concat(this.grid[i*this.col.length + j]);
            }
            console.log(_);
        }
    }
}