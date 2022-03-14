PRAGMA foreign_keys = ON;

CREATE TABLE Art (
    	ArtNavn TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE ForedlingsMetode (
    	Navn TEXT PRIMARY KEY NOT NULL,
	Beskrivelse TEXT UNIQUE
);

CREATE TABLE Region (
	Region TEXT NOT NULL,
	Land TEXT NOT NULL,
	PRIMARY KEY (Region, Land)
);

CREATE TABLE Gard (
    	GardID INTEGER PRIMARY KEY NOT NULL,
	Navn TEXT NOT NULL,
    	MOH INTEGER NOT NULL,
    	Region TEXT NOT NULL,
	Land TEXT NOT NULL,
    	FOREIGN KEY (Region, Land)
        	REFERENCES Region (Region, Land)
			ON DELETE RESTRICT
);

CREATE TABLE KaffeBrenneri (
    	BrenneriID INTEGER PRIMARY KEY NOT NULL,
    	Navn TEXT NOT NULL
);

CREATE TABLE Bruker (
    	Epost TEXT PRIMARY KEY NOT NULL,
    	Fornavn TEXT NOT NULL,
    	Etternavn TEXT NOT NULL,
    	Passord TEXT NOT NULL
);

CREATE TABLE FerdigBrentKaffe (
    	Navn TEXT NOT NULL,
    	Dato TEXT NOT NULL,
    	Beksrivelse TEXT NOT NULL,
    	Kilopris INTEGER NOT NULL ,
    	BrenneriID INTEGER NOT NULL,
	PartiID INTEGER NOT NULL,
	PRIMARY KEY (Navn, BrenneriID),
	FOREIGN KEY (BrenneriID)
        	REFERENCES KaffeBrenneri (BrenneriID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (PartiID)
		REFERENCES KaffeParti (PartiID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE KaffeSmaking (
    	epost TEXT NOT NULL,
    	BrentKaffeID INTEGER NOT NULL,
    	Notat TEXT,
  	Poeng INTEGER NOT NULL,
    	Dato TEXT,
    	PRIMARY KEY (epost, BrentKaffeID),
    	FOREIGN KEY (epost)
        	REFERENCES Bruker (epost)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION,
    	FOREIGN KEY (BrentKaffeID)
        	REFERENCES FerdigBrentKaffe (BrentKaffeID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION
);

CREATE TABLE KaffeBonner (
    	KaffeBonneID INTEGER PRIMARY KEY NOT NULL,
    	Navn TEXT NOT NULL
);

CREATE TABLE KaffeParti (
    	PartiID INTEGER PRIMARY KEY NOT NULL,
    	InnhostningAr INTEGER NOT NULL,
    	Gard INTEGER NOT NULL,
    	ForedlingsMetode TEXT NOT NULL,
    	FOREIGN KEY (ForedlingsMetode)
        	REFERENCES ForedlingsMetode (Navn)
			ON DELETE RESTRICT,
    	FOREIGN KEY (Gard)
        	REFERENCES Gard (GardID)
			ON DELETE RESTRICT
);

CREATE TABLE Kjoper (
    	BrenneriID INTEGER NOT NULL,
    	PartiId INTEGER NOT NULL,
    	Kilopris INTEGER NOT NULL,
    	PRIMARY KEY (BrenneriID, PartiID),
    	FOREIGN KEY (BrenneriID)
        	REFERENCES KaffeBrenneri (BrenneriID)
            		ON DELETE CASCADE
        	    	ON UPDATE NO ACTION,
    	FOREIGN KEY (PartiID)
        	REFERENCES KaffeParti (PartiID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTIOn
);

CREATE TABLE TilhorerArt (
    	ArtNavn TEXT NOT NULL,
    	KaffeBonneID INTEGER NOT NULL,
    	PRIMARY KEY (ArtNavn, KaffeBonneID),
    	FOREIGN KEY (ArtNavn)
        	REFERENCES Art (ArtNavn)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION,
    	FOREIGN KEY (KaffeBonneID)
        	REFERENCES KaffeBonner (KaffeBonneID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION
);

CREATE TABLE BonneForedles (
    	KaffeBonneID INTEGER NOT NULL,
    	Navn TEXT NOT NULL,
    	PRIMARY KEY (KaffeBonneID, Navn),
    	FOREIGN KEY (KaffeBonneID)
        	REFERENCES KaffeBonner (KaffeBonneID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION,
    	FOREIGN KEY (Navn)
        	REFERENCES ForedlingsMetode (Navn)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION
);

CREATE TABLE DyrketAv (
    	KaffeBonneID INTEGER NOT NULL,
    	GardID INTEGER NOT NULL,
    	PRIMARY KEY (KaffeBonneID, GardID),
    	FOREIGN KEY (KaffeBonneID)
        	REFERENCES KaffeBonner (KaffeBonneID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION,
    	FOREIGN KEY (GardID)
        	REFERENCES Gard (GardID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION
);

CREATE TABLE Har (
    	KaffeBonneID INTEGER NOT NULL,
    	PartiID INTEGER NOT NULL,
    	PRIMARY KEY (KaffeBonneID, PartiID),
    	FOREIGN KEY (KaffeBonneID)
        	REFERENCES KaffeBonner (KaffeBonneID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION,
    	FOREIGN KEY (PartiID)
        	REFERENCES KaffeParti (PartiID)
            		ON DELETE CASCADE
            		ON UPDATE NO ACTION
);
		
