# Setup command prompt
export PS1="\n\[\e[36m\]\u\e[97m in \[\e[93;1m\]\w\[\e[m\]\$(parse_git_branch)\n\$"
export CLICOLOR=1
export LSCOLORS=HxCxfxgxbxhxhxbxbxHxHx
alias ls='ls -GFh'

# Setup Bash completion
if [ -f $(brew --prefix)/etc/bash_completion ]; then
	/Users/dcook/.bash_profile
. $(brew --prefix)/etc/bash_completion
fi

# Functions, functions, functions
mkcd()
{
    mkdir -p -- "$1" &&
      cd -P -- "$1"
}

parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

