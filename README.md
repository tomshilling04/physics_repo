# Accretion signatures during supermassive black hole mergers  


Masters MPhys research project investigating accretion dynamics during supermassive black hole (SMBH) mergers using 
Smoothed Particle Hydrodynamics (SPH) simulations.  

This work explores the physical validity of the **snowplough effect**, a proposed 
enhancement in accretion onto a primary SMBH immediately prior to merger. The project analyses simulation outputs generated with the [PHANTOM SPH](https://github.com/danieljprice/phantom) code by Daniel Price, and compares results against previous studies to investigate whether the effect is a genuine physical process or a numerical artefact.  

## Project Overview  

During the late stages of a SMBH merger, gravitational wave emission causes the binary orbit to decay rapidly. Previous work suggested that this inspiral may compress gas within a circumprimary accretion disc, producing a large increase in accretion rate known as the snowplough effect.  
This project:
- Reproduces and compares results from previous studies.
- Analyses PHANTOM SPH simulation outputs.
- Calculates viscous and gravitational wave timescales.
- Determines the decoupling separation of SMBH binary systems.
- Investigates the influence of artificial viscosity, disc viscosity, resolution, and sink radius parameters.
- Evaluates whether the snowplough effect remains under physically motivated simulation condition.

## Key Findings  

- The snowplough effect was recovered under specific simulation conditions.
- Increasing simulation resolution strengthened the observed accretion enhancement.
- Accretion behaviour converged across different secondary sink radii.
- Results indicate the snowplough effect is a physical process rather than a numerical artefact caused by enlarged sink radii.
- The work has implications for identifying electromagnetic counterparts to gravitational wave detections by the future LISA mission.

## Repository Structure  

```text
├── Analysis/
│   ├── Simulation analysis notebooks
│   ├── Accretion rate calculations
│   ├── Disc evolution analysis
│   └── Visualisation scripts
│
│
├── figures/
│   ├── Simulation figures
│   ├── Accretion rate plots
│   ├── Surface density profiles
│   └── Thesis figures
│
├── weekly_summaries/
│   └── Research progress logs and development notes
│
└── README.md
```

## Research Context  
This repository supports the Masters thesis:  
Accretion signatures during supermassive black hole mergers - seen on my [Linkedin](https://www.linkedin.com/in/thomas-leon-shilling/)  
conducted as part of the MPhys Physics with Astrophysics programme at the University of Leeds.  
A summary of the project can be found in the associated dissertation. The work focuses on understanding accretion-disc behaviour during SMBH mergers and the potential observational signatures relevant to future gravitational wave observatories such as LISA.  

## Notes  
Simulation data files are not included due to there size. This repository contains the analysis notebooks, calculations, visualisations, and supporting research documentation used throughout the project.  
