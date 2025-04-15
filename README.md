## Girafa

### Passo a Passo para obtenção do contorno

- Utilizando um kernel de 15, utilizamos uma imagem com gradiente para obter o contorno
- `img_grad = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)`

### Resultado

<div style="display: flex; justify-content: center; gap: 14px;">
  <div style="display: flex; flex-direction: column; align-items: center; justify-content-center; gap: 10px">
    <img src="generatedImages\Gradiente_Girafa.png" width="50%" />
    <p>Gradiente da Girafa</p>
  </div>
  <div style="display: flex; flex-direction: column; align-items: center; justify-content-center; gap: 10px">
    <img src="generatedImages\Contorno_Girafa.png" width="50%" />
    <p>Contorno da Girafa</p>
  </div>
</div>

## Avião

### Passo a Passo para obtenção do contorno

- Utilizando um kernel de 10, utilizamos uma imagem equalizada (melhorar separação entre sombra e o avião), com um blur (remover ruídos), com um Threshold Adaptativo (para sombra e iluminação desigual) e com um gradiente para obter o contorno
```
  img_eq = cv2.equalizeHist(img_gray)
  img_blur = cv2.GaussianBlur(img_eq, (5, 5), 0)
  img_adaptive_thresh = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
  img_grad = cv2.morphologyEx(img_adaptive_thresh, cv2.MORPH_GRADIENT, kernel)
```

### Resultado

<div style="display: flex; justify-content: center; gap: 14px;">
  <div style="display: flex; flex-direction: column; align-items: center; justify-content-center; gap: 10px">
    <img src="generatedImages\Gradiente_Aviao.png" width="50%" />
    <p>Gradiente do Avião</p>
  </div>
  <div style="display: flex; flex-direction: column; align-items: center; justify-content-center; gap: 10px">
    <img src="generatedImages\Contorno_Aviao.png" width="50%" />
    <p>Contorno do Avião</p>
  </div>
</div>

## Satélite

### Passo a Passo para obtenção do contorno

- Utilizando um kernel de 40, utilizamos uma imagem com gradiente para obter o contorno
- `img_grad = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)`

### Resultado

<div style="display: flex; justify-content: center; gap: 14px;">
  <div style="display: flex; flex-direction: column; align-items: center; justify-content-center; gap: 10px">
    <img src="generatedImages\Gradiente_Satelite.png" width="50%" />
    <p>Gradiente do Satélite</p>
  </div>
  <div style="display: flex; flex-direction: column; align-items: center; justify-content-center; gap: 10px">
    <img src="generatedImages\Contorno_Satelite.png" width="50%" />
    <p>Contorno do Satélite</p>
  </div>
</div>