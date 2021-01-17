dirSaveFiles=models
rm -r ${dirSaveFiles}
mkdir ${dirSaveFiles}

# FICHER -> https://drive.google.com/file/d/1neSH23XUAvqdSDHNDq5T47mPoLmsz8yM/view?usp=sharing
fileId=1neSH23XUAvqdSDHNDq5T47mPoLmsz8yM
fileName=modeloFisherFaces.xml
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${dirSaveFiles}/${fileName}

# Eigen -> https://drive.google.com/file/d/1FEz7aIyIZ4TCgohMlw6kQ4kKN4e5hkpz/view?usp=sharing
fileId=1FEz7aIyIZ4TCgohMlw6kQ4kKN4e5hkpz
fileName=modeloEigenFaces.xml
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${dirSaveFiles}/${fileName}

# LBPH -> https://drive.google.com/file/d/1HfotvvT3MJtXBoDGSBnMZKV2nkDAHas_/view?usp=sharing
fileId=1HfotvvT3MJtXBoDGSBnMZKV2nkDAHas_
fileName=modeloLBPH.xml
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${dirSaveFiles}/${fileName}
