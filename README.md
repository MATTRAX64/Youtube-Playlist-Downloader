# 🎬 Media Toolkit

Media Toolkit est une application Python avec interface graphique permettant de manipuler facilement vos médias :

✅ Conversion vidéo, image et audio  
✅ Téléchargement de playlists YouTube  
✅ Modification des couleurs des images  
✅ Détection automatique de FFmpeg et support GPU CUDA  

---

# 📦 Fonctionnalités

## 1️⃣ Format Changer

Convertit automatiquement tous les fichiers d’un dossier.

### Formats supportés :

#### 🎥 Vidéo
- mp4
- mkv
- mov
- webm
- avi

#### 🖼️ Image
- jpg
- png
- webp
- avif
- tiff
- bmp
- gif

#### 🎵 Audio
- mp3
- flac
- aac
- ogg
- opus
- wav
- m4a

### Comment ça marche ?

1. Ouvrir l'onglet **Format Changer**
2. Choisir un dossier
3. Choisir les formats de sortie
4. Cliquer sur **Lancer la conversion**

Le programme :

- analyse tous les fichiers
- détecte leur type
- convertit automatiquement
- remplace les anciens fichiers

Si une carte NVIDIA est détectée, CUDA est utilisé automatiquement 🚀

---

# 2️⃣ YouTube Playlist

Télécharge une playlist complète avec la qualité de votre choix.

### Formats disponibles :

- MP3 192 kbps
- MP3 320 kbps
- FLAC Lossless
- AAC 320k
- Opus 320k
- MP4 meilleure qualité
- MP4 1080p
- MP4 720p

### Comment ça marche ?

1. Ouvrir l'onglet **YouTube**
2. Coller le lien d'une playlist
3. Choisir le format
4. Choisir le dossier de sortie
5. Cliquer sur **Télécharger**

Le logiciel :

- récupère toutes les vidéos
- crée un dossier avec le nom de la playlist
- télécharge chaque vidéo automatiquement

---

# 3️⃣ Color Changer

Permet de modifier des images en masse.

### Réglages disponibles :

- Saturation
- Luminosité
- Contraste
- Gamma

### Comment ça marche ?

1. Choisir un fichier ou un dossier
2. Régler les valeurs
3. Choisir le format de sortie
4. Cliquer sur **Lancer**

Le programme traite toutes les images automatiquement.

---

# ⚙️ Paramètres

Tous les outils utilisent la même configuration.

### FFmpeg

Media Toolkit utilise FFmpeg pour :

- convertir les vidéos
- convertir l'audio
- modifier les images

Vous devez sélectionner votre fichier :

`ffmpeg.exe`

Le programme peut aussi le détecter automatiquement.

---

# 🛠 Installation

## 1. Cloner le projet

```bash
git clone https://github.com/VOTRE-NOM/MediaToolkit.git
cd MediaToolkit
```

## 2. Installer Python

Python 3.8 ou plus récent.

---

## 3. Installer les dépendances

```bash
pip install yt-dlp
```

Tkinter est déjà inclus sur Windows.

---

## 4. Lancer

```bash
python MediaToolkit.py
```

---

# 📁 Sauvegarde

Les paramètres sont enregistrés automatiquement dans :

```json
mediatoolkit.json
```

Ce fichier sauvegarde :

- chemin FFmpeg
- dossiers utilisés
- formats sélectionnés
- réglages couleurs

---

# 🚀 Technologies utilisées

- Python
- Tkinter
- FFmpeg
- yt-dlp
- CUDA (optionnel)

---

# 💡 Notes

⚠ FFmpeg est obligatoire.  
Téléchargement :

https://ffmpeg.org/download.html

⚠ Pour YouTube, yt-dlp est installé automatiquement si nécessaire.

---

# 📜 Licence

Projet libre d'utilisation.
