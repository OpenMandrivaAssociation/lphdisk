Name:		lphdisk
Version:	0.9.1
Release:	%mkrel 5
Summary:	Format Phoenix NoteBIOS hibernation partitions under Linux
License:	Artistic
Group:		System/Kernel and hardware
URL:		http://www.procyon.com/~pda/lphdisk
Source0:	http://www.procyon.com/~pda/lphdisk/%{name}-%{version}.tar.bz2
Patch0:		lphdisk-0.9.1-debian.patch
Patch1:		lphdisk-0.9.1-lrmi.patch
ExclusiveArch:	%ix86
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
lphdisk is a linux reimplementation of the PHDISK.EXE (DOS) utility provided
with most Phoenix NoteBIOS-equipped laptop models.  It will properly format a
NoteBIOS hibernation partition (type A0) to make it usable by the BIOS for
suspending to disk, avoiding the need to use buggy and outdated DOS utilities 
to perform this configuration step.

PLEASE NOTE: this is a very old tool for very old laptops. Unless you're very
sure you need it...you probably don't. Move along, nothing to see here.

%prep
%setup -q
%patch0 -p1 -b .debian
%patch1 -p1 -b .lrmi

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sbindir}

install -m 755 lphdisk %{buildroot}%{_sbindir}
install -m 644 lphdisk.8 %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog CREDITS LICENSE NEWS README TODO
%{_sbindir}/lphdisk
%{_mandir}/man8/lphdisk.8.*

