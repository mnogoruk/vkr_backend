CREATE SCHEMA IF NOT EXISTS vkr;

CREATE TABLE IF NOT EXISTS vkr.specialization_category
(
    id   VARCHAR(30) PRIMARY KEY,
    name VARCHAR(512) NOT NULL
);

CREATE TABLE IF NOT EXISTS vkr.specialization
(
    id                         VARCHAR(30) PRIMARY KEY,
    name                       VARCHAR(512) NOT NULL,
    laboring                   BOOLEAN      NOT NULL,
    specialization_category_id VARCHAR(30)  NOT NULL,

    CONSTRAINT fk_specialization_category
        FOREIGN KEY (specialization_category_id)
            REFERENCES vkr.specialization_category (id)
);

CREATE TABLE IF NOT EXISTS vkr.vacancy_area
(
    id   VARCHAR(30) PRIMARY KEY,
    name VARCHAR(512) NOT NULL
);

CREATE TABLE IF NOT EXISTS vkr.vacancy_employer
(
    id   VARCHAR(30) PRIMARY KEY,
    name VARCHAR(512) NOT NULL
);


CREATE TABLE IF NOT EXISTS vkr.vacancy
(
    id                  VARCHAR(30) PRIMARY KEY,
    name                VARCHAR(512)             NOT NULL,
    alternate_url       VARCHAR(2048)            NULL,
    description_cleaned TEXT                     NULL,
    area_id             VARCHAR(30)              NULL,
    employer_id         VARCHAR(30)              NULL,
    official            BOOLEAN DEFAULT FALSE    NOT NULL,
    living              BOOLEAN DEFAULT FALSE    NOT NULL,
    vacation            BOOLEAN DEFAULT FALSE    NOT NULL,
    coworkers           BOOLEAN DEFAULT FALSE    NOT NULL,
    office              BOOLEAN DEFAULT FALSE    NOT NULL,
    education           BOOLEAN DEFAULT FALSE    NOT NULL,
    salary_bonus        BOOLEAN DEFAULT FALSE    NOT NULL,
    location            BOOLEAN DEFAULT FALSE    NOT NULL,
    extra               BOOLEAN DEFAULT FALSE    NOT NULL,
    growth              BOOLEAN DEFAULT FALSE    NOT NULL,
    tasks               BOOLEAN DEFAULT FALSE    NOT NULL,
    dms                 BOOLEAN DEFAULT FALSE    NOT NULL,
    social              BOOLEAN DEFAULT FALSE    NOT NULL,
    discount            BOOLEAN DEFAULT FALSE    NOT NULL,
    hours               BOOLEAN DEFAULT FALSE    NOT NULL,
    disko               BOOLEAN DEFAULT FALSE    NOT NULL,
    food                BOOLEAN DEFAULT FALSE    NOT NULL,
    remote              BOOLEAN DEFAULT FALSE    NOT NULL,
    drive               BOOLEAN DEFAULT FALSE    NOT NULL,
    hotel               BOOLEAN DEFAULT FALSE    NOT NULL,
    tech                BOOLEAN DEFAULT FALSE    NOT NULL,
    clothes             BOOLEAN DEFAULT FALSE    NOT NULL,
    sport               BOOLEAN DEFAULT FALSE    NOT NULL,
    published_at        TIMESTAMP WITH TIME ZONE NULL,
    created_at          TIMESTAMP WITH TIME ZONE NULL,

    CONSTRAINT fk_vacancy_area
        FOREIGN KEY (area_id)
            REFERENCES vkr.vacancy_area (id),

    CONSTRAINT fk_vacancy_employer
        FOREIGN KEY (employer_id)
            REFERENCES vkr.vacancy_employer (id)
);

CREATE TABLE IF NOT EXISTS vkr._m2m_vacancy_specialization
(
    vacancy_id        VARCHAR(30) NOT NULL,
    specialization_id VARCHAR(30) NOT NULL,

    CONSTRAINT fk_m2m_vacancy_vacancy_specialization
        FOREIGN KEY (vacancy_id)
            REFERENCES vkr.vacancy (id),

    CONSTRAINT fk_m2m_specialization_vacancy_specialization
        FOREIGN KEY (specialization_id)
            REFERENCES vkr.specialization (id)
);