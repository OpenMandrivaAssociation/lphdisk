%define name	lphdisk
%define version	0.9.1
%define release	2mdk

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Utility for formatting Phoenix NoteBIOS hibernation partitions under Linux
License:	Artistic
Group:		System/Kernel and hardware
Patch:		%{name}-0.9.1.source.patch.bz2
URL:		http://www.procyon.com/~pda/lphdisk
Source:		http://www.procyon.com/~pda/lphdisk/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExclusiveArch:	%ix86

%description
lphdisk is a linux reimplementation of the PHDISK.EXE (DOS) utility provided
with most Phoenix NoteBIOS-equipped laptop models.  It will properly format a
NoteBIOS hibernation partition (type A0) to make it usable by the BIOS for
suspending to disk, avoiding the need to use buggy and outdated DOS utilities 
to perform this configuration step.

%prep
%setup -q
%patch0 -p0 -b .newgcc

%build
%make

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}

install -m 755 lphdisk ${RPM_BUILD_ROOT}%{_sbindir}
install -m 644 lphdisk.8 ${RPM_BUILD_ROOT}%{_mandir}/man8

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc ChangeLog CREDITS LICENSE NEWS README TODO
%{_sbindir}/lphdisk
%{_mandir}/man8/lphdisk.8.*

