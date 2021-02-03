dirSaveFiles=models
rm -r ${dirSaveFiles}
mkdir ${dirSaveFiles}

# FICHER -> https://drive.google.com/file/d/1l7jd2U-UVL787sAuzDiBCMCRii2qZ3ug/view?usp=sharing
fileId=1l7jd2U-UVL787sAuzDiBCMCRii2qZ3ug
fileName=modelFisherFaces.xml
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${dirSaveFiles}/${fileName}

# Eigen -> https://drive.google.com/file/d/1jJQO5thrZyRvPKpfwMBtV-vNzvtAMwd7/view?usp=sharing
fileId=1jJQO5thrZyRvPKpfwMBtV-vNzvtAMwd7
fileName=modelEigenFaces.xml
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${dirSaveFiles}/${fileName}

# LBPH -> https://drive.google.com/file/d/1q4uk5mu97LQkknc6_ATUVEsGe8rETZf9/view?usp=sharing
fileId=1q4uk5mu97LQkknc6_ATUVEsGe8rETZf9
fileName=modelLBPH.xml
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${dirSaveFiles}/${fileName}
