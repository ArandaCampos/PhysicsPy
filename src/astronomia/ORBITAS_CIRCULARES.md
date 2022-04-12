## Órbitas Circulares (Satélites)

&emsp;Na astronomia, os satélites são definidos como corpos que movimentam-se ao redor de um corpo celeste, normalmente mais pesado, como planeta, e não há colisão. Os satélites podem ser classificados como naturais ou artificiais: como a Lua e a Estação Internacional por exemplo.<br>
&emsp;A única força sofrida pelo satélite em órbita é a gravidade. E para manter-se em orbita, precisa de uma velocidade precisa: nem pequena a ponto de sua trajetória colidir com o corpo orbitado e, nem superior a ponto de sair de órbita. Por isso, sabendo a distancia, podemos determinar com exatidão sua velocidade e consequentemente, sua trajetória. 

## Fórmulas importantes de Órbitas Circulares

| Fórmula | Descrição |
| --- | --- |
| g(orb) = GM / R² | g(orb), gravidade no satélite; G, constante gravitacional; M, massa do celeste orbitado; R, raio da trajetória |
| v² = Rg(orb) | v, velocidade; R, raio da trajetória; g(orb), gravidade no satélite |
| T = 2PiR / v | T, período; Pi, constante Pi; R, raio da trajetória; v, velocidade |
| theta = 2Pi / T | theta, angulo theta; Pi, constante Pi; T, período |
| P(x) = R * sen(theta) | P(x), posição no eixo x; R, raio da trajetória; theta, angulo |
| P(x) = R * cos(theta) | P(y), posição no eixo y; R, raio da trajetória; theta, angulo |

## Modo de usar.

![orbitas_circulares](https://user-images.githubusercontent.com/87876734/162813250-68674b44-5e53-4a55-914e-8a1c14c1391c.gif)

&emsp; Neste exemplo foi simulado a orbita da Lua, nosso único satélite natural. Observe que apesar da Lua ser visível a olho nu, ela se encontra muito distante da terra, aproximadamente 384.400 km. Outra informação interessante é o tempo que a Lua leva para completar uma volta em torno da Terra, que é de aproximadamento 27 dias.

## Tecnologias empregadas
* Python3
* Pygame
