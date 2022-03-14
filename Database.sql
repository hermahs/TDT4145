PRAGMA foreign_keys = ON;

CREATE TABLE Bruker (
    	Epost TEXT PRIMARY KEY NOT NULL,
    	Fornavn TEXT NOT NULL,
    	Etternavn TEXT NOT NULL,
    	Passord TEXT NOT NULL
);

CREATE TABLE Kaffesmaking (
    	Epost TEXT NOT NULL,
	KaffeNavn TEXT NOT NULL,
    	BrenneriID INTEGER NOT NULL,
    	Notat TEXT,
  	Poeng INTEGER NOT NULL,
    	Dato TEXT,
	
    	PRIMARY KEY (Epost, KaffeNavn, BrenneriID),
    	FOREIGN KEY (Epost)
        	REFERENCES Bruker (Epost)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION,
    	FOREIGN KEY (KaffeNavn, BrenneriID)
        	REFERENCES FerdigbrentKaffe (Navn, BrenneriID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION
	CHECK (Poeng >= 0 AND Poeng <= 10)
);

CREATE TABLE FerdigbrentKaffe (
    	Navn TEXT NOT NULL,
	BrenneriID INTEGER NOT NULL,
	Brenningsgrad TEXT NOT NULL,
    	Dato TEXT NOT NULL,
    	Beksrivelse TEXT NOT NULL,
    	KiloprisNOK INTEGER NOT NULL ,
	PartiID INTEGER NOT NULL,
	
	PRIMARY KEY (Navn, BrenneriID),
	FOREIGN KEY (PartiID)
		REFERENCES Kaffeparti (PartiID)
			ON DELETE CASCADE
			ON UPDATE NO ACTION,
	FOREIGN KEY (BrenneriID)
        	REFERENCES Kaffebrenneri (ID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION
	CHECK( Brenningsgrad IN ('mørk','middels','lys') )
);

CREATE TABLE Kaffebrenneri (
    	ID INTEGER PRIMARY KEY NOT NULL,
    	Navn TEXT NOT NULL
);

CREATE TABLE Kaffeparti (
    	ID INTEGER PRIMARY KEY NOT NULL,
    	InnhostningAr INTEGER NOT NULL,
	KiloprisUSD INTEGER NOT NULL,
    	GardID INTEGER NOT NULL,
    	ForedlingsNavn TEXT NOT NULL,
	
    	FOREIGN KEY (ForedlingsNavn)
        	REFERENCES Foredlingsmetode (Navn)
			ON DELETE RESTRICT,
    	FOREIGN KEY (GardID)
        	REFERENCES Gard (GardID)
			ON DELETE RESTRICT
);

CREATE TABLE Art (
    	Navn TEXT PRIMARY KEY NOT NULL
	
	CHECK ( Navn IN ('coffea arabica', 'coffea robusta', 'coffea liberica') )
);

CREATE TABLE KaffebonneType (
    	Navn TEXT PRIMARY KEY NOT NULL,
    	ArtNavn TEXT NOT NULL,
	
	FOREIGN KEY (ArtNavn)
        	REFERENCES Art (Navn)		
);

CREATE TABLE BestarAv (
    	KaffebonneNavn TEXT NOT NULL,
    	PartiID INTEGER NOT NULL,
	
    	PRIMARY KEY (KaffebonneNavn, PartiID),
    	FOREIGN KEY (KaffebonneNavn)
        	REFERENCES KaffebonneType (Navn)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION,
    	FOREIGN KEY (PartiID)
        	REFERENCES Kaffeparti (PartiID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION
);

CREATE TABLE Foredlingsmetode (
    	Navn TEXT PRIMARY KEY NOT NULL,
	Beskrivelse TEXT UNIQUE
);

CREATE TABLE Gard (
    	ID INTEGER PRIMARY KEY NOT NULL,
	Navn TEXT NOT NULL,
    	MeterOverHavet INTEGER NOT NULL,
    	Region TEXT NOT NULL,
	Land TEXT NOT NULL,
	
    	FOREIGN KEY (Region, Land)
        	REFERENCES Region (Region, Land)
			ON DELETE RESTRICT
);

CREATE TABLE DyrkesAv (
    	KaffebonneNavn TEXT NOT NULL,
    	GardID INTEGER NOT NULL,
	
    	PRIMARY KEY (KaffebonneNavn, GardID),
    	FOREIGN KEY (KaffebonneNavn)
        	REFERENCES KaffebonneType (Navn)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION,
    	FOREIGN KEY (GardID)
        	REFERENCES Gard (ID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION
);

CREATE TABLE Region (
	Region TEXT NOT NULL,
	Land TEXT NOT NULL,
	
	PRIMARY KEY (Region, Land)
);
