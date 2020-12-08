# shellcheck disable=SC2164
# shellcheck disable=SC2162

cd
cd PycharmProjects/alienclouds
pip freeze > requirements.txt
git config --global user.email "andriiburka@gmail.com"
git add .
git commit -m "No significant changes"
git push -u origin master
