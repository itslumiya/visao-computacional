## Girafa

### Passo a Passo para obtenção do contorno

- Utilizando um kernel de 15, utilizamos uma imagem com gradiente para obter o contorno
- `img_grad = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)`

### Resultado

<div style="display: flex; justify-content: center; gap: 14px;">
  <figure style="text-align: center; width: 50%">
    <img src="generatedImages\Gradiente_Girafa.png" width="50%" />
    <figcaption>Gradiente da Girafa</figcaption>
  </figure>
  <figure style="text-align: center; width: 50%">
    <img src="generatedImages\Contorno_Girafa.png" width="50%" />
    <figcaption>Contorno da Girafa</figcaption>
  </figure>
</div>