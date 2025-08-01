# ML-Movie-Recommender-System
Hey there 🙋🏻‍♂️!! This repo contains my Movie Recommender System based on Machine Learning (ML). You will get to see i) Data processing ii) ML (⊂ AI) techniques iii) Web development iv) Deployment, its a lot of work👷🏻! Enjoy your walk👣 through the repo, Feel free to raise PR if you think we can improve.

## Repository Structure
```
├── readme.md         # Must read to understand what is done
├── LICENSE           # Permissions
├── 
```

## Table Of contents
| S.No | Heading | What it conveys? |
|:---|:--|:--|
| 1 | [Introduction](#introduction)| Recommender systems, ML |

## Introduction

### Types Of Recommender Systems
1) Content based
    -  Recommending new content based on similarity with query + already watched content
    - Example: Youtube recommending test cricket video, as you searched for cricket
2) Collaborative filtering
    - Based on interests of user
    - Example: Based on history if A and B has high similarity, then if A watched something new then the new stuff can be recommended to B
3) Hybrid

### This Project
This repo builds **Content Based Movie Recommender System** using Machine Learning, which is cool😎!! The techniques used in here, can be used else where from document retreival to ecommerce development, from search engine to social media content.

```mermaid
graph TD;
    Data-->Preprocessing;
    Preprocessing-->ML-Model;
    ML-Model--> Web-Dev;
    Web-Dev--> Deploy;
```
