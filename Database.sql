CREATE TABLE Land (
    LandId INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    LandNavn TEXT NOT NULL
);

CREATE TABLE Art (
    ArtNavn TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE ForedlingsMetode (
    Navn TEXT PRIMARY KEY NOT NULL,
    Beskrivelse TEXT NOT NULL
);

CREATE TABLE Region (
    RegionID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    RegionNavn TEXT NOT NULL,
    Land INTEGER NOT NULL,
    FOREIGN KEY (Land)
        REFERENCES Land (LandId)
);

CREATE TABLE Gard (
    GardID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    MOH INTEGER NOT NULL,
    Region INTEGER NOT NULL,
    FOREIGN KEY (Region)
        REFERENCES Region (RegionId)
);

CREATE TABLE KaffeBrenneri (
    BrenneriID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    Navn TEXT NOT NULL
);

CREATE TABLE Bruker (
    epost TEXT PRIMARY KEY NOT NULL,
    fornavn TEXT NOT NULL,
    etternavn TEXT NOT NULL,
    passord TEXT NOT NULL,
    nasjonalitet INTEGER NOT NULL,
    FOREIGN KEY (nasjonalitet)
        REFERENCES Land (LandId)
);

CREATE TABLE FerdigBrentKaffe (
    BrentKaffeID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    Dato TEXT NOT NULL,
    Navn TEXT NOT NULL,
    Beksrivelse TEXT NOT NULL,
    Kilopris INTEGER NOT NULL ,
    BrenneriID INTEGER NOT NULL,
    FOREIGN KEY (BrenneriID)
        REFERENCES KaffeBrenneri (BrenneriID)
);

CREATE TABLE KaffeSmaking (
    epost TEXT NOT NULL,
    BrentKaffeID INTEGER NOT NULL,
    Notat TEXT NOT NULL,
    Poeng INTEGER NOT NULL,
    Dato TEXT NOT NULL,
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
    KaffeBonneID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    Navn TEXT NOT NULL,
);

CREATE TABLE KaffeParti (
    PartiID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    Innhøstningsår INTEGER NOT NULL,
    Gard INTEGER NOT NULL,
    ForedlingsMetode TEXT NOT NULL,
    FOREIGN KEY (ForedlingsMetode)
        REFERENCES ForedlingsMetode (Navn),
    FOREIGN KEY (Gard)
        REFERENCES Gard (GardID)
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

