from ApplicationMgr import ApplicationMgr

def main():
	integrator = ApplicationMgr()
	print("Are you ready?")
	integrator.CheckIf(None, integrator.EndApp)
	integrator.Read()
	integrator.SolveIntegrator()

if __name__ == "__main__":
    main()
