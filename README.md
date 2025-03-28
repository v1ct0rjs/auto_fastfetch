## Documentación de *auto_fastfetch*

Este script permite verificar dependencias necesarias y compilar e instalar [Fastfetch](vscode-file://vscode-app/opt/visual-studio-code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) de manera automatizada. Una vez instalado, lo ejecuta automáticamente.

### Requisitos previos

- Python 3.x
- Paquetes base de compilación (por ejemplo, `git`, `cmake`, `make`, `gcc`)

------

### Estructura de Archivos

```bash
auto_fastfetch/
├── auto_fastfetch.py     # Script principal
└── README.md             # (Este archivo de documentación, sugerido)
```



### Uso

 1. Clona o descarga el repositorio que contiene este script.

    ```bash
    git clone git@github.com:v1ct0rjs/auto_fastfetch.git
    ```

    

 2. Accede al directorio del repositorio git

    ```bash
    cd auto_fastfetch
    ```

    

 3. Concede permisos de ejecución al scrip

    ```bash
    chmod +x auto_fastfetch.py
    ```

    

 4. Ejecuta el script

    ```bash
    python auto_fastfetch.py
    ```

    

### Instalación en shells

**Bash**

```
# Edita tu archivo ~/.bashrc y agrega lo siguiente:
alias auto_fastfetch="/ruta/a/auto_fastfetch.py"

# (Opcional) Aplica los cambios:
source ~/.bashrc
```

**Zsh**

```
# En tu ~/.zshrc, agrega:
alias auto_fastfetch="/ruta/a/auto_fastfetch.py"

# Aplica los cambios:
source ~/.zshrc
```

**Fish**

```
# En tu archivo de configuración de fish (generalmente ~/.config/fish/config.fish):
alias auto_fastfetch "/ruta/a/auto_fastfetch.py"

# No olvides reiniciar tu sesión de fish o recargar la configuración:
source ~/.config/fish/config.fish
```

### Uso Posterior

- Una vez hecho el alias en tu shell preferido, puedes ejecutar:

  ```bash
  auto_fastfetch
  ```

- El script verificará si *fastfetch* ya está instalado y simplemente lo ejecutará sin mostrar mensajes adicionales.

- Si no encuentra *fastfetch*, instalará las dependencias y descargará el repositorio oficial para compilarlas.

------

### Ejemplo de Ejecución

![image-20250328112122525](/home/v1ct0r/auto_fastfetch/image-20250328112122525.png)

![image-20250328112154565](/home/v1ct0r/auto_fastfetch/image-20250328112154565.png)



------