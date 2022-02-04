source /usr/share/defaults/etc/profile
export PATH="$PATH:/home/martin/.local/bin:/usr/lib/openjdk-8/bin"

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# PS1="\[$(tput bold)\]\[\033[38;5;9m\]\u\[\033[38;5;213m\]@\[\033[38;5;208m\]\h:\[\033[38;5;6m\]\w\n \\$ "
PS1="\[\033[38;5;228m\]\u\[\033[38;5;7m\]@\[\033[38;5;159m\]\h \[\033[38;5;7m\]\w\n $\[$(tput sgr0)\] "

# Custom Aliases
alias update="sudo apt update && sudo apt upgrade && sudo apt autoremove && sudo apt autoclean"
alias pull="./git_pull.sh"
alias gitpass="echo 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"

PROMPT_DIRTRIM=3
