export PS1="\w"

__git_ps1 ()
{
	local b="$(git symbolic-ref HEAD 2>/dev/null)";
	if [ -n "$b" ]; then
		printf " (%s)" "${b##refs/heads/}";
	fi
}

PS1="\h\$(__git_ps1)$ "
