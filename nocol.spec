Summary:	Network Operation Center On-Line
Summary(pl):	Centrum Operacji Sieciowych
Name:		nocol
Version:	4.3.1
Release:	2
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
Source0:	http://www.netplex-tech.com/software/nocol/downloads/%{name}-%{version}.tar.gz
URL:		http://www.netplex-tech.com/software/nocol/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NOCOL/SNIPS (Network Operation Center On-Line) is a network monitoring
package that runs on Unix platforms and is capable of monitoring
network and system variables such as ICMP or RPC reachability, RMON
variables, nameservers, ethernet load, port reachability, host
performance, SNMP traps, modem line usage, appletalk & novell
routes/services, BGP peers, syslog files, etc. The software is
extensible and new monitors can be added easily.

%description -l pl
NOCOL/SNIPS (Network Operation Center On-Line) jest pakietem
monitoruj�cym sie� dzia��j�cym na uniksach, kt�ry mo�e monitorowa�
sie� i takie cechy systemu jak osi�galno�� ICMP czy RPC, zmienne RMON,
serwery DNS, obci��enie sieci, osi�galno�� port�w, wydajno��
komputera, pu�apki SNMP, obci��enie linii modemowej, serwisy AppleTalk
i Novell, po��czenia BGP, pliki log�w itp. To oprogramowanie jest
rozszerzalne i nowe monitory mog� by� dodawane w prosty spos�b.

%prep
%setup -q

%build
cat | ./Configure <<EOF
%{_prefix}
%{_mandir}

localhost
/bin/mail
root@localhost
root@localhost
gcc
%{rpmcflags} -I/usr/include/ncurses
yacc
/usr/bin/perl
EOF

%{__make} << EOF
make
EOF

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
