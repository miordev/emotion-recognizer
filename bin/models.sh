dirSaveFiles=models
rm -r ${dirSaveFiles}
mkdir ${dirSaveFiles}

# FICHER -> https://drive.google.com/file/d/1vQSYNSUOPY1QmdLpUxjmWhcM8jRxPKzd/view?usp=sharing
fileId=1vQSYNSUOPY1QmdLpUxjmWhcM8jRxPKzd
fileName=modelFisherFaces.xml
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${dirSaveFiles}/${fileName}

# Eigen -> https://drive.google.com/file/d/1rpaS5-iuun7BB4cQo0YUkME4IZ3TFiA0/view?usp=sharing
fileId=1rpaS5-iuun7BB4cQo0YUkME4IZ3TFiA0
fileName=modelEigenFaces.xml
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${dirSaveFiles}/${fileName}

# LBPH -> https://drive.google.com/file/d/1IwrY8G1Y8rOlCN-y90GKKKghVhpb4XlH/view?usp=sharing
fileId=1IwrY8G1Y8rOlCN-y90GKKKghVhpb4XlH
fileName=modelLBPH.xml
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${dirSaveFiles}/${fileName}
