Summary:	Project managment tool
Summary(pl.UTF-8):	Narzędzie do zarządzania projektem
Name:		faces-pm
Version:	0.11.4
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/faces-project/%{name}-%{version}.tar.gz
# Source0-md5:	fcd1246914a47d02407aa4ed9b767c6a
URL:		http://faces.homeip.net/
BuildRequires:	python-modules >= 2.2.1
%pyrequires_eq	python-modules
BuildRequires:	python-matplotlib
Requires:	python-matplotlib
Requires:	python-wxPython >= 2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
faces is a powerful and flexible project management tool. It not only offers
many extraordinary features like multiple resource balancing algorithms and
multi scenario planing, but can also be easily extended and customized.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

#py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/faces
%{py_sitescriptdir}/*egg-info
%dir %{py_sitescriptdir}/faces
%{py_sitescriptdir}/faces/*.py[co]
%dir %{py_sitescriptdir}/faces/charting
%{py_sitescriptdir}/faces/charting/*.py[co]
%dir %{py_sitescriptdir}/faces/gui
%{py_sitescriptdir}/faces/gui/*.py[co]
%dir %{py_sitescriptdir}/faces/gui/editor
%dir %{py_sitescriptdir}/faces/gui/editor/*.py[co]
%{py_sitescriptdir}/faces/gui/resources
%dir %{py_sitescriptdir}/faces/howtos
#%{py_sitescriptdir}/faces/howtos/*.py[co]
%{py_sitescriptdir}/faces/howtos/*.txt
%dir %{py_sitescriptdir}/faces/lib
%{py_sitescriptdir}/faces/lib/*.py[co]
%{py_sitescriptdir}/faces/templates
%dir %{py_sitescriptdir}/faces/tools
%{py_sitescriptdir}/faces/tools/*.py[co]
%dir %{py_sitescriptdir}/metapie
%dir %{py_sitescriptdir}/metapie/*.py[co]
%dir %{py_sitescriptdir}/metapie/gui
%dir %{py_sitescriptdir}/metapie/gui/*.py[co]
%dir %{py_sitescriptdir}/metapie/gui/wxcontrols
%dir %{py_sitescriptdir}/metapie/gui/wxcontrols/*.py[co]
%{py_sitescriptdir}/metapie/resources
