# shellcheck disable=SC2164
# shellcheck disable=SC2162

cd
cd PycharmProjects/alienclouds
echo
echo
echo "THIS COMMAND WILL COMPLETELY DESTROY THE CURRENT VERSION AND WILL REVERT TO THE PREVIOUS.
IF YOU ARE SURE, TYPE THE VERSION YOU WANT & PUNCH ENTER"
read msg
git reset --hard "$msg"
echo "__DONE__"



# MORE ABOUT THIS
#https://www.git-tower.com/learn/git/faq/restore-repo-to-previous-revision/