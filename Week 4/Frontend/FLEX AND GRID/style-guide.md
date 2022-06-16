# Front-end Style Guide

## Layout

The designs were created to the following widths:

- Mobile: 375px
- Desktop: 1440px

## Colors

### Primary

Bright orange: hsl(31, 77%, 52%)
Dark cyan: hsl(184, 100%, 22%)
Very dark cyan: hsl(179, 100%, 13%)

### Neutral

Transparent white (paragraphs): hsla(0, 0%, 100%, 0.75)
Very light gray (background, headings, buttons): hsl(0, 0%, 95%)

## Typography

### Body Copy

- Font size: 15px

### Font

- Family: [Lexend Deca](https://fonts.google.com/specimen/Lexend+Deca)
- Weights: 400

- Family: [Big Shoulders Display](https://fonts.google.com/specimen/Big+Shoulders+Display)
- Weights: 700

main{
  width:50%;
  margin: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-family: var(--Deca-family);
}
h3{
  font-family: var(--Deca-family);
  color: var(bhb);
  font-size: var(--font-size);
}
.sedans{
  background-color: var(--Bright-orange);
  color: var(--p-white);
  padding:4em;
  height: 50%;
  width: 100%;
  border-top-left-radius: 6px;
  border-bottom-left-radius: 6px

}
.sedans button {
  display: inline-block;
  background: white;
  border: 2px solid var(--Bright-orange);
  padding:0.3rem;
  border-radius: 2rem;
  line-height: 1.3;
  color: var(--Bright-orange);
  font-weight: 500;
  font-size: 15px;
}
.sedans button:hover {
  background: var(--Bright-orange);
  color: white;
  border: 2px solid white;
  transition: 0.4s;
}


.suvs{
  background-color: var(--Dark-cyan);
  color: var(--p-white);
  padding: 4em;
  height: 50%;
  width: 100%;
}
.suvs button {
  display: inline-block;
  background: white;
  border: 2px solid var(--Dark-cyan);
  padding: 0.5rem;
  border-radius: 5rem;
  line-height: 1.3;
  color: var(--Dark-cyan);
  font-weight: 100;
}
.suvs button:hover {
  background: var(--Dark-cyan);
  color: white;
  border: 2px solid white;
  transition: 0.4s;
}

.luxury{
  background-color: var(--Very-dark-cyan);
  color: var(--p-white);
  padding: 4em;
  height: 50%;  
  border-top-right-radius: 6px;
  border-bottom-right-radius: 6px;
 

} 
.luxury button {
  display: inline-block;
  background: white;
  border: 2px solid var(--Dark-cyan);
  padding: 0.5rem;
  border-radius: 3rem;
  color: var(--Dark-cyan);
  font-weight: 100;
  
}
.luxury button:hover {
  background: var(--Dark-cyan);
  color: white;
  border: 2px solid white;
  transition: 0.4s;
}

